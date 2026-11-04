#!/usr/bin/env python3
import html as html_lib
import json
import os
import re
import urllib.parse
import urllib.request
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://www.aym-inc.org/wp-json/wp/v2/posts?per_page=100&_embed"
IMG_DIR = os.path.join(ROOT, "assets", "img", "blog")
UA = "Mozilla/5.0 (compatible; AYM static site builder)"
SITE_HOSTS = {"www.aym-inc.org", "aym-inc.org"}

PAGE_MAP = {
    "": "index.html",
    "about": "about.html",
    "about-us": "about.html",
    "mission": "about.html",
    "history": "about.html",
    "team": "about-team.html",
    "leadership": "about-team.html",
    "chapter": "chapter.html",
    "building-an-aym-chapter": "chapter.html",
    "contact": "contact.html",
    "contact-us": "contact.html",
    "donate": "donate.html",
    "donate1": "donate.html",
    "donate-now": "donate.html",
    "events": "events.html",
    "projects": "projects.html",
    "our-work": "projects.html",
    "where-we-work": "where-we-work.html",
    "volunteer": "volunteer.html",
    "volunteer-apply": "volunteer-apply.html",
    "volunteer-fellowship": "volunteer-fellowship.html",
    "aym-shop": "store.html",
    "shop": "store.html",
    "store": "store.html",
    "focus-art": "focus-art.html",
    "art": "focus-art.html",
    "focus-agriculture": "focus-agriculture.html",
    "agriculture": "focus-agriculture.html",
    "focus-ecotourism": "focus-ecotourism.html",
    "ecotourism": "focus-ecotourism.html",
    "focus-ecotourism-forest-safari": "focus-ecotourism-forest-safari.html",
    "forest-safari": "focus-ecotourism-forest-safari.html",
    "focus-education": "focus-education.html",
    "education": "focus-education.html",
    "focus-entrepreneurship": "focus-entrepreneurship.html",
    "entrepreneurship": "focus-entrepreneurship.html",
    "focus-health": "focus-health.html",
    "healthcare": "focus-health.html",
    "health": "focus-health.html",
    "focus-technology": "focus-technology.html",
    "technology": "focus-technology.html",
}

IMG_CACHE = {}

TITLE_OVERRIDES = {
    "building-the-twenty-first-century-african-youth-movement-aymvirtual-conference-on-youth-employment-and-righteous-ragefirst-annual-virtual-conference": (
        "Building the Twenty-First Century African Youth Movement (AYM) "
        "Virtual Conference on Youth, Employment, and Righteous Rage: "
        "First Annual Virtual Conference"
    )
}


def fetch(url, binary=False):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as response:
        data = response.read()
    return data if binary else data.decode("utf-8")


def esc(value):
    return html_lib.escape(str(value), quote=True)


def plain_text(rendered):
    text = re.sub(r"<[^>]+>", " ", rendered)
    text = html_lib.unescape(text)
    text = re.sub(r"\[\s*&hellip;\s*\]", " ", text)
    text = text.replace("\u200b", "").replace("\ufeff", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def post_title(post):
    return plain_text(post["title"]["rendered"])


def post_date(post):
    stamp = datetime.fromisoformat(post["date"])
    return stamp.strftime("%B %d, %Y").replace(" 0", " ")


def post_author(post):
    try:
        return post["_embedded"]["author"][0]["name"]
    except (KeyError, IndexError, TypeError):
        return "AYM Team"


def post_excerpt(post, limit=190):
    text = plain_text(post["excerpt"]["rendered"])
    if len(text) < 40:
        text = plain_text(post["content"]["rendered"])
    if len(text) > limit:
        text = text[: limit + 1].rsplit(" ", 1)[0].rstrip(",.;:") + "…"
    return text


def choose_srcset(srcset, max_width=1200):
    entries = [
        (int(width), url)
        for url, width in re.findall(r"(\S+)\s+(\d+)w", srcset)
    ]
    if not entries:
        return None
    under = [entry for entry in entries if entry[0] <= max_width]
    if under:
        return max(under)
    return min(entries)


def localize_image(url, name):
    url = html_lib.unescape(url)
    if url in IMG_CACHE:
        return IMG_CACHE[url]

    path = urllib.parse.urlparse(url).path
    ext = os.path.splitext(path)[1].lower()
    if ext not in (".jpg", ".jpeg", ".png", ".webp", ".gif"):
        ext = ".jpg"
    filename = re.sub(r"[^a-z0-9-]+", "-", name.lower()).strip("-") + ext
    dest = os.path.join(IMG_DIR, filename)
    rel = "assets/img/blog/" + filename

    if not os.path.exists(dest):
        try:
            data = fetch(url, binary=True)
            if len(data) < 200:
                raise ValueError("response too small")
            os.makedirs(IMG_DIR, exist_ok=True)
            with open(dest, "wb") as handle:
                handle.write(data)
            print("  +", rel)
        except Exception as exc:
            print("  ! could not download", url, "-", exc)
            IMG_CACHE[url] = url
            return url

    IMG_CACHE[url] = rel
    return rel


def featured_image(post):
    media_list = post.get("_embedded", {}).get("wp:featuredmedia") or []
    if not media_list or not media_list[0].get("source_url"):
        return None
    media = media_list[0]
    sizes = media.get("media_details", {}).get("sizes", {})
    src = media["source_url"]
    width = media.get("media_details", {}).get("width")
    height = media.get("media_details", {}).get("height")
    for key in ("large", "medium_large", "full"):
        if key in sizes and sizes[key].get("source_url"):
            src = sizes[key]["source_url"]
            width = sizes[key].get("width") or width
            height = sizes[key].get("height") or height
            break
    src = localize_image(src, "post-%s-cover" % post["id"])
    alt = media.get("alt_text") or post_title(post)
    return {"src": src, "alt": alt, "width": width, "height": height}


def map_url(url):
    if url.startswith(("http://", "https://")):
        parsed = urllib.parse.urlparse(url)
        if parsed.netloc.lower() not in SITE_HOSTS:
            return None
        path = parsed.path
    elif url.startswith("/"):
        path = url
    else:
        return None

    slug = path.strip("/")
    if slug in ("aym-blog", "blog") or slug.startswith("aym-blog/page/"):
        return "blog.html"
    if slug in BLOG_FILES:
        return BLOG_FILES[slug]
    if slug in PAGE_MAP:
        return PAGE_MAP[slug]
    return None


def localize_links(markup):
    def replace(match):
        quote, url = match.group(1), match.group(2)
        local = map_url(html_lib.unescape(url))
        return 'href=%s"%s"' % (quote, esc(local)) if local else match.group(0)

    return re.sub(r'href=(["\'])([^"\']+)\1', replace, markup)


def transform_content(markup, post):
    markup = re.sub(r"<!--.*?-->", "", markup, flags=re.S)
    markup = re.sub(r"<(script|style|svg)\b.*?</\1>", "", markup, flags=re.S | re.I)
    markup = localize_links(markup)

    counter = [0]

    def replace_image(match):
        tag = match.group(0)
        src = re.search(r'\bsrc="([^"]+)"', tag)
        if not src:
            return ""
        chosen = html_lib.unescape(src.group(1))
        width = re.search(r'\bwidth="(\d+)"', tag)
        height = re.search(r'\bheight="(\d+)"', tag)
        original_width = int(width.group(1)) if width else None
        original_height = int(height.group(1)) if height else None
        width = original_width
        height = original_height
        alt = re.search(r'\balt="([^"]*)"', tag)
        alt = html_lib.unescape(alt.group(1)) if alt else ""
        srcset = re.search(r'\bsrcset="([^"]+)"', tag)
        if srcset:
            picked = choose_srcset(html_lib.unescape(srcset.group(1)))
            if picked:
                width, chosen = picked
                if original_width and original_height and width:
                    height = round(original_height * width / original_width)
        counter[0] += 1
        local = localize_image(chosen, "post-%s-%s" % (post["id"], counter[0]))
        attrs = ' src="%s" alt="%s"' % (esc(local), esc(alt))
        if width:
            attrs += ' width="%s"' % width
        if height:
            attrs += ' height="%s"' % height
        return "<img%s loading=\"lazy\" decoding=\"async\">" % attrs

    markup = re.sub(r"<img\b[^>]*>", replace_image, markup, flags=re.I)

    def replace_iframe(match):
        tag = match.group(0)
        src = re.search(r'\bsrc="([^"]+)"', tag)
        if not src:
            return ""
        src = html_lib.unescape(src.group(1)).replace("&#038;", "&")
        if not re.search(r"(youtube\.com|youtu\.be|vimeo\.com)", src):
            return ""
        return (
            '<iframe src="%s" title="Video" loading="lazy" '
            'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
            'gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>'
        ) % esc(src)

    markup = re.sub(
        r"<iframe\b[^>]*>.*?</iframe>", replace_iframe, markup, flags=re.S | re.I
    )

    markup = re.sub(r"</?div\b[^>]*>", "", markup, flags=re.I)
    markup = re.sub(
        r'\s(?:class|id|style|decoding|fetchpriority|srcset|sizes|data-[\w-]+)="[^"]*"',
        "",
        markup,
        flags=re.I,
    )
    markup = re.sub(r"<(/?)h4\b", r"<\1h3", markup, flags=re.I)
    markup = re.sub(r"<(/?)h6\b", r"<\1h4", markup, flags=re.I)

    empty_p = re.compile(r"<p\b[^>]*>(?:\s|&nbsp;|<br\s*/?>)*</p>", re.I)
    for _ in range(4):
        markup = empty_p.sub("", markup)

    def merge_list_items(match):
        items = re.findall(r"<li>(.*?)</li>", match.group(0), flags=re.S)
        merged = []
        for item in items:
            item = item.strip()
            if (
                merged
                and re.search(r"[A-Za-z,]$", merged[-1])
                and re.match(r"[a-z]", item)
            ):
                merged[-1] = merged[-1] + " " + item
            else:
                merged.append(item)
        return "<ul>" + "".join("<li>%s</li>" % item for item in merged) + "</ul>"

    markup = re.sub(r"<ul>.*?</ul>", merge_list_items, markup, flags=re.S)
    markup = re.sub(r"<br\s*/?>\s*(?=[a-z])", " ", markup)
    markup = re.sub(r"\n{3,}", "\n\n", markup)
    return markup.strip()


def read_time(markup):
    text = plain_text(markup)
    words = len(re.findall(r"\b[\w'-]+\b", text))
    return max(2, round(words / 200))


def shell(title, description, main_html):
    page = BASE
    page = re.sub(
        r"<title>.*?</title>", "<title>%s</title>" % esc(title), page, count=1, flags=re.S
    )
    page = re.sub(
        r'<meta name="description" content="[^"]*">',
        '<meta name="description" content="%s">' % esc(description),
        page,
        count=1,
    )
    page = MAIN_RE.sub(
        lambda match: match.group(1) + "\n" + main_html.strip() + "\n" + match.group(3),
        page,
        count=1,
    )
    return page


def write_page(filename, markup):
    with open(os.path.join(ROOT, filename), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(markup)
    print("  =", filename)


def cover_markup(cover, css_class="post-cover"):
    if not cover:
        return ""
    attrs = ' src="%s" alt="%s"' % (esc(cover["src"]), esc(cover["alt"]))
    if cover.get("width"):
        attrs += ' width="%s"' % cover["width"]
    if cover.get("height"):
        attrs += ' height="%s"' % cover["height"]
    return '<img class="%s"%s>' % (css_class, attrs)


def main():
    global BASE, MAIN_RE, BLOG_FILES

    print("Fetching posts…")
    posts = json.loads(fetch(API))
    posts.sort(key=lambda item: item["date"], reverse=True)
    posts = [post for post in posts if post.get("status", "publish") == "publish"]

    BLOG_FILES = {post["slug"]: "blog-%s.html" % post["slug"] for post in posts}
    BASE = open(os.path.join(ROOT, "store.html"), encoding="utf-8").read()
    MAIN_RE = re.compile(r'(<main id="main">)(.*?)(</main>)', re.S)

    prepared = []
    print("Preparing posts and images…")
    for post in posts:
        content = transform_content(post["content"]["rendered"], post)
        title = TITLE_OVERRIDES.get(post["slug"], post_title(post))
        prepared.append(
            {
                "post": post,
                "title": title,
                "date": post_date(post),
                "author": post_author(post),
                "excerpt": post_excerpt(post),
                "content": content,
                "cover": featured_image(post),
                "read": read_time(content),
                "file": BLOG_FILES[post["slug"]],
            }
        )

    cards = []
    for item in prepared:
        href = item["file"]
        if item["cover"]:
            media = (
                '<a class="blog-card__media" href="%s" tabindex="-1" aria-hidden="true">'
                '<img class="card__img" src="%s" alt="%s" loading="lazy">'
                "</a>"
            ) % (esc(href), esc(item["cover"]["src"]), esc(item["cover"]["alt"]))
        else:
            media = (
                '<a class="blog-card__media card__img card__img--placeholder" '
                'href="%s" tabindex="-1" aria-hidden="true"></a>' % esc(href)
            )
        cards.append(
            '<article class="card blog-card">%s<div class="card__body">'
            '<div class="card__tag">%s &middot; %s min read</div>'
            '<h3 class="card__title"><a href="%s">%s</a></h3>'
            '<p class="card__text">%s</p>'
            '<a class="card__link" href="%s">Read the story &rarr;</a>'
            "</div></article>"
            % (
                media,
                esc(item["date"]),
                item["read"],
                esc(href),
                esc(item["title"]),
                esc(item["excerpt"]),
                esc(href),
            )
        )

    blog_main = """
<section class="section section--cream blog-head">
  <div class="container">
    <p class="eyebrow">Blog</p>
    <h1>Stories from the movement.</h1>
    <p class="lead">Dispatches from AYM's work across Africa and the diaspora — youth leadership, education, ecotourism, enterprise and culture.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid-3 blog-grid">
      %s
    </div>
  </div>
</section>
""" % "\n      ".join(cards)

    write_page(
        "blog.html",
        shell(
            "Blog | Twenty-First Century African Youth Movement (AYM)",
            "Stories from AYM's work across Africa and the diaspora: youth leadership, education, ecotourism, enterprise and culture.",
            blog_main,
        ),
    )

    for index, item in enumerate(prepared):
        href = item["file"]
        newer = prepared[index - 1] if index > 0 else None
        older = prepared[index + 1] if index + 1 < len(prepared) else None
        nav_cards = []
        if newer:
            nav_cards.append(
                '<a class="post-nav__card" href="%s"><span>Newer story</span>'
                "<strong>%s</strong></a>"
                % (esc(newer["file"]), esc(newer["title"]))
            )
        if older:
            nav_cards.append(
                '<a class="post-nav__card" href="%s"><span>Older story</span>'
                "<strong>%s</strong></a>"
                % (esc(older["file"]), esc(older["title"]))
            )

        cover = (
            '<section class="section post-cover-wrap"><div class="container">%s</div></section>'
            % cover_markup(item["cover"])
            if item["cover"]
            else ""
        )
        nav = ""
        if nav_cards:
            nav = (
                '<nav class="post-nav" aria-label="More stories">%s</nav>'
                % "".join(nav_cards)
            )

        main_html = """
<section class="section section--cream post-head">
  <div class="container post-head__inner">
    <p class="eyebrow"><a href="blog.html">Blog</a> &middot; %s</p>
    <h1 class="post-title">%s</h1>
    <p class="post-meta"><span>By %s</span><span>%s min read</span></p>
  </div>
</section>
%s
<section class="section">
  <div class="container">
    <article class="post-body">
%s
    </article>
    <div class="post-footer">
      <a class="btn btn--outline" href="blog.html">&larr; All Stories</a>
      <a class="btn btn--brand" href="donate.html">Support Our Work</a>
    </div>
    %s
  </div>
</section>
""" % (
            esc(item["date"]),
            esc(item["title"]),
            esc(item["author"]),
            item["read"],
            cover,
            item["content"],
            nav,
        )

        description = item["excerpt"] or item["title"]
        write_page(
            href,
            shell("%s | AYM Blog" % item["title"], description[:160], main_html),
        )

    print("Done: %s posts" % len(prepared))


if __name__ == "__main__":
    main()

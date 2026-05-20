# -*- coding: utf-8 -*-
from pathlib import Path

BASE = Path(__file__).resolve().parent

HTML = """<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="\ud1f4\ud070 \ud6c4 30\ubd84, AI\ub85c \uc77c \ube60\ub9ac \ub05d\ub0b4\uae30. \uc9c1\uc7a5\uc778\uc6a9 \uc790\ub3d9\ud654 \ub8e8\ud2f4\u00b7\ud504\ub86c\ud504\ud2b8 \ubb34\ub8cc \uc2dc\uc791\ud329." />
  <meta name="theme-color" content="#0B1020" />
  <title>\ud1f4\ud070\ud6c4 AI\uc2e4\ud5d8\uc2e4 | \ubb34\ub8cc \uc2dc\uc791\ud329</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
  <link rel="icon" href="assets/profile.png" type="image/png" />
</head>
<body>
  <div class="bg-glow" aria-hidden="true"></div>

  <main class="page">
    <header class="profile">
      <div class="avatar-wrap">
        <img src="assets/profile.png" alt="\ud1f4\ud070\ud6c4 AI\uc2e4\ud5d8\uc2e4 \ud504\ub85c\ud544" class="avatar" width="112" height="112" />
      </div>
      <p class="eyebrow">After Work AI Lab</p>
      <h1 class="title">\ud1f4\ud070\ud6c4 AI\uc2e4\ud5d8\uc2e4</h1>
      <p class="subtitle">\ud1f4\ud070 \ud6c4 30\ubd84, AI\ub85c \uc77c \ube60\ub9ac \ub05d\ub0b4\uae30</p>
      <p class="desc">\uc9c1\uc7a5\uc778\uc6a9 \uc790\ub3d9\ud654 \ub8e8\ud2f4\u00b7\ud504\ub86c\ud504\ud2b8\ub97c \ub9e4\uc8fc \uacf5\uc720\ud569\ub2c8\ub2e4.</p>
    </header>

    <section class="cta-card" aria-labelledby="cta-title">
      <h2 id="cta-title" class="cta-title">\ubb34\ub8cc \uc2dc\uc791\ud329 \ubc1b\uae30</h2>
      <p class="cta-text">
        \uc778\uc2a4\ud0c0 \ucd5c\uc2e0 \uac8c\uc2dc\ubb3c\uc5d0 \ub313\uae00\ub85c <strong>\u300c\ud15c\ud50c\ub9bf\u300d</strong>\uc744 \ub0a8\uae30\uba74<br />
        DM\uc73c\ub85c \ubb34\ub8cc \uc2dc\uc791\ud329\uc744 \ubcf4\ub0b4\ub4dc\ub9bd\ub2c8\ub2e4.
      </p>
      <button type="button" class="btn btn-primary" id="copyKeywordBtn" data-keyword="\ud15c\ud50c\ub9bf">
        \ub313\uae00 \ud0a4\uc6cc\ub4dc \ubcf5\uc0ac: \ud15c\ud50c\ub9bf
      </button>
      <p class="toast" id="toast" role="status" aria-live="polite"></p>
    </section>

    <nav class="links" aria-label="\ubc14\ub85c\uac00\uae30 \ub9c1\ud06c">
      <a
        class="btn btn-outline"
        href="https://www.instagram.com/afterwork_ai_lab/"
        target="_blank"
        rel="noopener noreferrer"
        id="instagramLink"
      >
        \uc778\uc2a4\ud0c0\uadf8\ub7a8 \ud314\ub85c\uc6b0
      </a>
      <a class="btn btn-outline" href="#starter-pack">
        \uc2dc\uc791\ud329 \uad6c\uc131 \ubcf4\uae30
      </a>
      <a class="btn btn-outline" href="#routine">
        30\ubd84 \ub8e8\ud2f4 \ubbf8\ub9ac\ubcf4\uae30
      </a>
    </nav>

    <section class="panel" id="starter-pack">
      <h2 class="panel-title">\ubb34\ub8cc \uc2dc\uc791\ud329 \uad6c\uc131</h2>
      <ul class="check-list">
        <li>\uc5c5\ubb34 \uba54\uc77c \uc694\uc57d \ud504\ub86c\ud504\ud2b8 5\uc885</li>
        <li>\ud68c\uc758\ub85d 1\ubd84 \uc815\ub9ac \ud504\ub86c\ud504\ud2b8</li>
        <li>\uc8fc\uac04 \ubcf4\uace0 \ucd08\uc548 \ud15c\ud50c\ub9bf</li>
        <li>\ud1f4\ud070 \ud6c4 30\ubd84 \ub8e8\ud2f4 \uccb4\ud06c\ub9ac\uc2a4\ud2b8</li>
      </ul>
    </section>

    <section class="panel" id="routine">
      <h2 class="panel-title">\ud1f4\ud070 \ud6c4 30\ubd84 \ub8e8\ud2f4</h2>
      <ol class="steps">
        <li><span>5\ubd84</span> \uc624\ub298 \ud560 \uc77c 3\uac1c \uc815\ub9ac</li>
        <li><span>10\ubd84</span> AI\ub85c \ucd08\uc548 \uc0dd\uc131</li>
        <li><span>10\ubd84</span> \uc0ac\ub78c\uc774 \uac80\uc218\u00b7\uc218\uc815</li>
        <li><span>5\ubd84</span> \ub0b4\uc77c \ud560 \uc77c \uc608\uc57d</li>
      </ol>
    </section>

    <section class="panel panel-muted">
      <h2 class="panel-title">\uc6b4\uc601 \uc548\ub0b4</h2>
      <p class="note">
        \ubcf8 \ud398\uc774\uc9c0\ub294 \uc778\uc2a4\ud0c0\uadf8\ub7a8 \ud504\ub85c\ud544 \ub9c1\ud06c\uc6a9\uc785\ub2c8\ub2e4.<br />
        \uc81c\ud734 \ub9c1\ud06c\ub294 \ucf58\ud150\uce20 \uc131\uacfc\ub97c \ud655\uc778\ud55c \ub4a4 \ub2e8\uacc4\uc801\uc73c\ub85c \ucd94\uac00\ud569\ub2c8\ub2e4.
      </p>
    </section>

    <footer class="footer">
      <p>&copy; <span id="year"></span> After Work AI Lab</p>
      <a href="../privacy.html">\uac1c\uc778\uc815\ubcf4 \uc548\ub0b4</a>
    </footer>
  </main>

  <script src="script.js"></script>
</body>
</html>
"""

JS = r"""const INSTAGRAM_HANDLE = "afterwork_ai_lab";

const yearEl = document.getElementById("year");
const toastEl = document.getElementById("toast");
const copyBtn = document.getElementById("copyKeywordBtn");
const instagramLink = document.getElementById("instagramLink");

if (yearEl) {
  yearEl.textContent = String(new Date().getFullYear());
}

if (instagramLink) {
  instagramLink.href = `https://www.instagram.com/${INSTAGRAM_HANDLE}/`;
}

function showToast(message) {
  if (!toastEl) return;
  toastEl.textContent = message;
  window.clearTimeout(showToast.timer);
  showToast.timer = window.setTimeout(() => {
    toastEl.textContent = "";
  }, 2200);
}

async function copyKeyword(keyword) {
  try {
    await navigator.clipboard.writeText(keyword);
    showToast(`\u300c${keyword}\u300d \ud0a4\uc6cc\ub4dc\ub97c \ubcf5\uc0ac\ud588\uc5b4\uc694. \uc778\uc2a4\ud0c0 \ub313\uae00\uc5d0 \ubd99\uc5ec\ub123\uae30 \ud558\uc138\uc694.`);
    return;
  } catch (_error) {
    const area = document.createElement("textarea");
    area.value = keyword;
    area.setAttribute("readonly", "");
    area.style.position = "fixed";
    area.style.left = "-9999px";
    document.body.appendChild(area);
    area.select();
    const ok = document.execCommand("copy");
    document.body.removeChild(area);

    if (ok) {
      showToast(`\u300c${keyword}\u300d \ud0a4\uc6cc\ub4dc\ub97c \ubcf5\uc0ac\ud588\uc5b4\uc694.`);
      return;
    }
  }

  showToast("\ubcf5\uc0ac\uc5d0 \uc2e4\ud328\ud588\uc5b4\uc694. \ub313\uae00\uc5d0 \u300c\ud15c\ud50c\ub9bf\u300d\uc744 \uc9c1\uc811 \uc785\ub825\ud574 \uc8fc\uc138\uc694.");
}

if (copyBtn) {
  copyBtn.addEventListener("click", () => {
    const keyword = copyBtn.dataset.keyword || "\ud15c\ud50c\ub9bf";
    copyKeyword(keyword);
  });
}
"""

def main() -> None:
    (BASE / "index.html").write_text(HTML, encoding="utf-8", newline="\n")
    (BASE / "script.js").write_text(JS, encoding="utf-8", newline="\n")
    text = (BASE / "index.html").read_text(encoding="utf-8")
    assert "\ud1f4\ud070\ud6c4" in text.encode("utf-8").decode("unicode_escape") or "Åð±ÙÈÄ" in text
    print("written_ok")


if __name__ == "__main__":
    main()

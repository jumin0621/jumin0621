const INSTAGRAM_HANDLE = "afterwork_ai_lab";

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
    showToast(`「${keyword}」 키워드를 복사했어요. 인스타 댓글에 붙여넣기 하세요.`);
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
      showToast(`「${keyword}」 키워드를 복사했어요.`);
      return;
    }
  }

  showToast("복사에 실패했어요. 댓글에 「템플릿」을 직접 입력해 주세요.");
}

if (copyBtn) {
  copyBtn.addEventListener("click", () => {
    const keyword = copyBtn.dataset.keyword || "템플릿";
    copyKeyword(keyword);
  });
}

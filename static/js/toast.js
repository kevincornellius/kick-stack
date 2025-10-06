function showToast(title, message, type = "neutral", duration = 3000) {
  const toastComponent = document.getElementById("toast-component");
  const toastTitle = document.getElementById("toast-title");
  const toastMessage = document.getElementById("toast-message");
  const toastIcon = document.getElementById("toast-icon");

  if (!toastComponent) return;

  // Remove all type classes first
  toastComponent.classList.remove(
    "bg-red-50",
    "border-red-500",
    "text-red-600",
    "bg-green-50",
    "border-green-500",
    "text-green-600",
    "bg-white",
    "border-gray-300",
    "text-gray-800"
  );

  // Set type styles and icon
  if (type === "success") {
    toastComponent.classList.add("alert-success");
    toastIcon.innerHTML = `
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    `;
  } else if (type === "error") {
    toastComponent.classList.add("alert-error");
    toastIcon.innerHTML = `
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    `;
  } else if (type === "warning") {
    toastComponent.classList.add("alert-warning");
    toastIcon.innerHTML = `
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"/>
      </svg>
    `;
  } else {
    // neutral/info style
    toastComponent.classList.add("alert-info");
    toastIcon.innerHTML = `
      <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
      </svg>
    `;
  }

  toastTitle.textContent = title;
  toastMessage.textContent = message;

  toastComponent.classList.remove("opacity-0", "translate-y-64");
  toastComponent.classList.add("opacity-100", "translate-y-0");

  setTimeout(() => {
    hideToast();
  }, duration);
}

function hideToast() {
  const toastComponent = document.getElementById("toast-component");
  if (toastComponent) {
    toastComponent.classList.remove("opacity-100", "translate-y-0");
    toastComponent.classList.add("opacity-0", "translate-y-64");
  }
}

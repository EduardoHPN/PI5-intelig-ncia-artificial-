document.addEventListener("DOMContentLoaded", () => {
  const TEST_MODE = true;  // ← Mantenha true para testes, false em produção

  const form = document.getElementById("doc-form");
  if (!form) return;

  const overlay = document.getElementById("pdf-loading-overlay");
  const spinner = overlay.querySelector(".spinner");
  const completeMsg = overlay.querySelector(".loading-complete");
  const closeBtn = overlay.querySelector("#pdf-close-btn");

  closeBtn.addEventListener("click", () => overlay.classList.add("hidden"));

  form.addEventListener("submit", async e => {
    e.preventDefault();
    overlay.classList.remove("hidden");
    spinner.classList.remove("hidden");
    completeMsg.classList.add("hidden");

    if (TEST_MODE) {
      console.log("TEST_MODE ativo: não chamando a API");
      // simula uma “chamada” com 1s de delay
      setTimeout(() => {
        spinner.classList.add("hidden");
        completeMsg.textContent = "✅ Concluído (TEST MODE)";
        completeMsg.classList.remove("hidden");
      }, 1000);
      return;  // MUITO IMPORTANTE: garante que o fetch nunca rode
    }

    try {
      const formData = new FormData(form);
      const response = await fetch(form.action, {
        method: "POST",
        headers: {
          "X-CSRFToken": form.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: formData
      });

      if (!response.ok) throw response;

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "peticao_completa.pdf";
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);

      spinner.classList.add("hidden");
      completeMsg.classList.remove("hidden");
    } catch (err) {
      spinner.classList.add("hidden");
      let msg = "❌ Falha ao gerar";
      if (err instanceof Response && err.status === 400) {
        const data = await err.json();
        msg = data.detail || msg;
      }
      completeMsg.textContent = msg;
      completeMsg.classList.remove("hidden");
    } finally {
      // mantém overlay até usuário fechar manualmente ou timeout
      // opcional: comente a linha abaixo se quiser fechar só pelo botão
      // setTimeout(() => overlay.classList.add("hidden"), 3000);
    }
  });
});

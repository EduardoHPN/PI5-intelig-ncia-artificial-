document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("doc-form");
  if (!form) return;

  const overlay = document.getElementById("pdf-loading-overlay");
  const spinner = overlay.querySelector(".spinner");
  const completeMsg = overlay.querySelector(".loading-complete");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    // Mostrar overlay
    overlay.classList.remove("hidden");
    spinner.classList.remove("hidden");
    completeMsg.classList.add("hidden");

    try {
      const formData = new FormData(form);
      const response = await fetch(form.action, {   // << usamos form.action aqui
        method: "POST",
        headers: {
          "X-CSRFToken": form.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: formData
      });

      if (!response.ok) throw new Error("Erro ao gerar PDF");

      const blob = await response.blob();
      const url = URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "peticao_completa.pdf";
      document.body.appendChild(a);
      a.click();
      a.remove();
      URL.revokeObjectURL(url);

      // feedback de concluído
      spinner.classList.add("hidden");
      completeMsg.classList.remove("hidden");
    } catch (err) {
      console.error(err);
      spinner.classList.add("hidden");
      completeMsg.textContent = "❌ Falha ao gerar";
      completeMsg.classList.remove("hidden");
    } finally {
      setTimeout(() => overlay.classList.add("hidden"), 3000);
    }
  });
});

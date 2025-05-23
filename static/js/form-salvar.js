function monitorarFormulario(form) {
    const interval = 2000;
    let ultimoSnapshot = "";

    setInterval(() => {
        const dados = {};
        for (const elemento of form.elements) {
            if (elemento.name) {
                if (elemento.type === "checkbox" || elemento.type === "radio") {
                    dados[elemento.name] = elemento.checked;
                } else {
                    dados[elemento.name] = elemento.value;
                }
            }
        }

        const jsonAtual = JSON.stringify(dados);
        if (jsonAtual !== ultimoSnapshot) {
            localStorage.setItem("dadosFormularioCliente", jsonAtual);
            ultimoSnapshot = jsonAtual;
        }
    }, interval);
}

function carregarFormulario(form) {
    const dadosSalvos = localStorage.getItem("dadosFormularioCliente");
    if (!dadosSalvos) return;

    const dados = JSON.parse(dadosSalvos);
    for (const elemento of form.elements) {
        if (elemento.name && dados.hasOwnProperty(elemento.name)) {
            if (elemento.type === "checkbox" || elemento.type === "radio") {
                elemento.checked = dados[elemento.name];
            } else {
                elemento.value = dados[elemento.name];
            }
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (form) {
        carregarFormulario(form);
        monitorarFormulario(form);

        form.addEventListener("submit", () => {
            localStorage.removeItem("dadosFormularioCliente");
        });
    }
});

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    const botaoSubmit = form?.querySelector("button[type='submit']");

    if (form) {
        carregarFormulario(form);
        monitorarFormulario(form);

        form.addEventListener("submit", () => {
            localStorage.removeItem("dadosFormularioCliente");
        });

        if (botaoSubmit) {
            botaoSubmit.addEventListener("click", () => {
                localStorage.removeItem("dadosFormularioCliente");
            });
        }
    }
});


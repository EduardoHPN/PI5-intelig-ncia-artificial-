    // Configuração do Firebase
    const firebaseConfig = {
      apiKey: "AIzaSyDUHVA75qtKwKFGQDdMKb1S0QaH8q4OhcM",
      authDomain: "projetointegrador5-27fb6.firebaseapp.com",
      projectId: "projetointegrador5-27fb6",
      storageBucket: "projetointegrador5-27fb6.appspot.com",
      messagingSenderId: "331147732123",
      appId: "1:331147732123:web:f24f497c6f856c30ee123e",
      measurementId: "G-4W95E8MNBG"
    };
  
    // Inicializa o Firebase
    firebase.initializeApp(firebaseConfig);
  
    // Função para pegar o CSRF token
    function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
            break;
          }
        }
      }
      return cookieValue;
    }
  
    // Captura o formulário e adiciona evento de submit
    const loginForm = document.getElementById("loginForm");
    loginForm.addEventListener("submit", function(e) {
      e.preventDefault(); // Evita recarregar a página
  
      const email = document.getElementById("emailLogin").value;
      const senha = document.getElementById("senhaLogin").value;
  
      firebase.auth().signInWithEmailAndPassword(email, senha)
      .then((userCredential) => {
        const user = userCredential.user;
        const uid = user.uid;
    
        // Enviar UID para o backend
        fetch("/autenticar/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")  // se usar CSRF
          },
          body: JSON.stringify({ uid: uid })
        })
        .then(response => {
          if (response.redirected) {
            window.location.href = response.url;  // redireciona se for o caso
          }
        });
      })
      .catch((error) => {
        alert("Erro ao fazer login");
        console.error(error);
      });    
    });

    // Formulário de cadastro
    const cadastroForm = document.getElementById("cadastroForm");
    cadastroForm.addEventListener("submit", function(e) {
      e.preventDefault();

      const email = document.getElementById("emailCad").value;
      const senha = document.getElementById("senhaCad").value;
      const confirmarSenha = document.getElementById("confirmarSenhaCad").value;

      if (senha !== confirmarSenha) {
        alert("As senhas não coincidem!");
        return;
      }

      firebase.auth().createUserWithEmailAndPassword(email, senha)
        .then((userCredential) => {
          alert("Cadastro realizado com sucesso!");
          window.location.href = "/home/";
        })
        .catch((error) => {
          alert("Erro ao cadastrar: " + error.message);
        });
    });
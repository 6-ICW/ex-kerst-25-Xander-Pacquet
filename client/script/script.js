// zorg voor een gepast benaming van je variabelen
// ik heb in jou code niet door welke type elementen je uit de html aanspreekt

const beforeLogin = document.querySelector("#beforLogin");
const afterLogin = document.querySelector("#afterLogin");
const login = document.querySelector("#login");
const change = document.querySelector("#change");

// button? over welke button gaat het?
const button = document.querySelector("#button");

button.addEventListener("click", (e) => {
  const dataForm = new FormData(login);

  // de opbouw van je dataobject is '{email, password}'
  // Die komen niet overeend met de nodige velden in de API {login, password}
  const data = Object.fromEntries(dataForm);

  console.log(data);

  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  // na een tip kwam je tot de juiste URL.
  fetch("https://ex-kerst-2025.onrender.com/user/", options)
    .then((res) => res.json())
    .then((data) => {
      console.log(data);
      // Onderstaande vond je op internet, maar naar wat was je op zoek?
      e.target.reset();
    });
});

change.onsubmit = (e) => {
  e.preventDefault();

  // in de FormData(change) zit geen id
  const id = new FormData(change).get("id");

  // const options= {}
  // fetch(url,options)
  // data loggen
};

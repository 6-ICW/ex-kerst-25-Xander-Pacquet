

const beforeLogin = document.querySelector("#beforLogin")
const afterLogin = document.querySelector("#afterLogin")
const login = document.querySelector("#login")
const change = document.querySelector("#change")
const button = document.querySelector("#button")

button.addEventListener("click",(e)=>{
    

    const dataForm = new FormData(login)
    const data  = Object.fromEntries(dataForm)

    console.log(data);
    

    const options =  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };
  fetch("https://ex-kerst-2025.onrender.com/user/",options)
  .then(res=>res.json())
  .then(data=>{
    console.log(data)
    e.target.reset()
    
  })

})


change.onsubmit = (e)=>{
  e.preventDefault()

  const id = new FormData(change).get("id")

  const options= {}
  fetch(url,options)
  data loggen
}






const beforeLogin = document.querySelector("#beforLogin")
const afterLogin = document.querySelector("#afterLogin")
const login = document.querySelector("#login")
const change = document.querySelector("#change")
const button = document.querySelector("#button")

button.addEventListener((e)=>{
    e.preventDefault()

    const dataForm = new FormData(beforeLogin)
    const data  = Object.fromEntries(dataForm)

    console.log(data);
    

    const options =  {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };
  fetch("https://ex-kerst-2025.onrender.com/",options)
  .then(res=>res.json())
  .then(data=>{
    console.log(data)
    e.target.reset()
    
  })
})




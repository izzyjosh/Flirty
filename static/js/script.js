const copyButton = document.querySelector(".clipboard")
const shareButton = document.querySelector(".sharebutton")
const catItem = document.querySelectorAll(".cat-item")
const quotePara = document.querySelectorAll(".quote-p")
const favoriteButton = document.querySelector(".fav")
const favIcon = document.querySelector(".fav-icon")



// index  category view
for (let i = 0; i < catItem.length; i++) {
 catItem[i].addEventListener("click", () => {
  const catId = catItem[i].getAttribute("data-id")
  console.log(catId)
  const nextPage = window.location + `category-quote/${catId}/`
  window.location.href = nextPage
 })
}
// quote from category view
for (let i = 0; i < quotePara.length; i++) {
 quotePara[i].addEventListener("click", () => {
  const quoteId = quotePara[i].getAttribute("data-id")
  const nextPage = window.location.origin + `/quote-detail/${quoteId}/`
  console.log(nextPage)
  location.assign(nextPage)
 })
}

favIcon.addEventListener("click", () => {
 const nextPage = window.location.origin + `/favorite/`
 location.assign(nextPage)
})

// Copy To Clipboard
copyButton.addEventListener("click", () => {
 const clipText = document.querySelector(".cliptext").textContent

 navigator.clipboard.writeText(clipText).then(() => {
  console.log("copied successfully ")
 }).catch((err) => {
  console.log("Error", err)
 })
 alert("Text copied successfully ")
})

// sharing to other apps
shareButton.addEventListener("click", () => {
 const clipText = document.querySelector(".cliptext").textContent

 if (navigator.share) {
  navigator.share({
   url: window.location,
   text: clipText
  })
  .then(() => {
   console.log("shared successfully ")
  })
  .catch((error) => {
   console.log("Error:", error)
  })
 } else {
  alert("Web share is not supported in this browser ")
 }
})

//saving favourite text to localstorage
favoriteButton.addEventListener("click", () => {
 const id = favoriteButton.getAttribute("data-id")
 const clipText = document.querySelector(".cliptext").textContent
 localStorage.setItem(`quote${id}`, clipText)
 favoriteButton.setAttribute("class", "bi bi-heart-fill fav");
})
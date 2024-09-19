// document.getElementById('task-form').addEventListener('submit', async function(event) {
//     event.preventDefault(); // Zapobiega domyślnej akcji formularza
    
//     const title = document.getElementById('title').value;
//     const description = document.getElementById('description').value;
    
//     const response = await fetch('/tasks/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ title, description })
//     });
    
//     if (response.redirected) {
//         window.location.href = response.url;
//     } else {
//         const result = await response.json();
//         alert(result.msg); // Wyświetla komunikat o sukcesie
//     }
// })

console.log('Skrypt działa!');
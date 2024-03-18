
document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    document.getElementById('loading').style.display = 'block';
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        if (!response.ok) {
            throw new Error('Failed to upload image');
        }
        const data = await response.text();
        console.log(data);
        
        if (data.includes("Approved:")) {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('approved-output-heading').innerHTML = `<h2>Approved</h2>`;
            document.getElementById('approved-output').innerHTML = `<p>${data}</p>`;
            openPopup("approved");
        }
        if (data.includes("Denied:")) {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('denied-output-heading').innerHTML = `<h2>Denied</h2>`;
            document.getElementById('denied-output').innerHTML = `<p>${data}</p>`;
            openPopup("denied");
        }
        
        // Reset the form
        this.reset(); // Reset the form fields
        
        // Clear the output area after 2 seconds
        // setTimeout(() => {
        //     document.getElementById('output').innerHTML = '';
        // }, 2000);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('output').innerHTML = `<p id="error-message">Error: ${error.message}</p>`;
    }
});
document.getElementById('proc_cheque').addEventListener('click', async function() {
    console.log('Checked Button clicked');
    
        window.location.href = "/process_checked"; // Redirect to p_cheque.html
   
});

function openPopup(status){
    console.log('openPopupcalled');
    if(status==="approved"){
        console.log('Approved');
        let popup = document.getElementById("popup-approved");
        popup.classList.add("open-popup");
    }
    if(status==="denied"){
        console.log('Denied');
        let popup = document.getElementById("popup-denied");
        popup.classList.add("open-popup");
    }
    
}
function closePopup(status){
    if(status==="approved"){
        let popup = document.getElementById("popup-approved");
        popup.classList.remove("open-popup");
    }
    if(status==="denied"){
        let popup = document.getElementById("popup-denied");
        popup.classList.remove("open-popup");
    }
}

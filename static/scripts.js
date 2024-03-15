document.getElementById('upload-form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        if (!response.ok) {
            throw new Error('Failed to upload image');
        }
        const data = await response.text();
        document.getElementById('output').innerHTML = `<p>Image uploaded successfully: ${data}</p>`;
        
        // Reset the form
        this.reset(); // Reset the form fields
        
        // Clear the output area after 2 seconds
        setTimeout(() => {
            document.getElementById('output').innerHTML = '';
        }, 2000);
    } catch (error) {
        console.error('Error:', error);
        document.getElementById('output').innerHTML = `<p id="error-message">Error: ${error.message}</p>`;
    }
});
document.getElementById('proc_cheque').addEventListener('click', async function() {
    console.log('Checked Button clicked');
    
        window.location.href = "/process_checked"; // Redirect to p_cheque.html
   
});


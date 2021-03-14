function deleteNote(noteId){
    // for sending a request to the back end
    fetch('/delete-note',{
        method:'POST',
        body: JSON.stringify({ noteId:noteId }),

    }).then((_res) => {
        // after getting the responce it will reload the window
        window.location.href = "/";
    })
}   
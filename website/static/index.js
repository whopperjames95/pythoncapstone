function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/personal_goals";
    });
}

// delete functions

function deleteTravel(noteId) {
    fetch("/delete-travel", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/travel";
    });
}

function deleteBucket(noteId) {
    fetch("/delete-bucket", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/bucket_list";
    });
}
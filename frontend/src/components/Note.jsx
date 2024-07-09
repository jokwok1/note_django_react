import React from "react"
import "../styles/Note.css"

const Note = ({note, onDelete}) => {
    // help use format the date to remove timezone, human-readable date format
    //"en-US" for US English. This typically formats the date as MM/DD/YYYY.
    const formattedDate = new Date(note.created_at).toLocaleDateString("en-US");
  
    return (
    <div className="note-container">
        <p className="note-title">{note.title}</p>
        <p className="note-content">{note.content}</p>
        <p className="note-date">{formattedDate}</p>
        <button className='delete-button' onClick={() => onDelete(note.id)}>
            Delete
        </button>
    </div>
  )
}

export default Note
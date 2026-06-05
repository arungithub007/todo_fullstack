import React, { useState, useEffect } from "react";
import { getTasks, addTask, updateTask, deleteTask } from "./api";

function App() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  useEffect(() => {
    refreshTasks();
  }, []);

  const refreshTasks = () => {
    getTasks().then(res => setTasks(res.data));
  };

  const handleAdd = () => {
    addTask(newTask).then(() => {
      refreshTasks();
      setNewTask("");
    });
  };

  const handleUpdate = (id) => {
    const updated = prompt("Enter new task:");
    if (updated) {
      updateTask(id, updated).then(() => refreshTasks());
    }
  };

  const handleDelete = (id) => {
    deleteTask(id).then(() => refreshTasks());
  };

  return (
    <div>
      <h1>Todo List</h1>
      <input value={newTask} onChange={e => setNewTask(e.target.value)} />
      <button onClick={handleAdd}>Add</button>
      <ul>
        {tasks.map(t => (
          <li key={t.id}>
            {t.task}
            <button onClick={() => handleUpdate(t.id)}>Edit</button>
            <button onClick={() => handleDelete(t.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

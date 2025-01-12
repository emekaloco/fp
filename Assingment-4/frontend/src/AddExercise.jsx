import React, { useState } from 'react';
import { addExercise } from './api';

// form for adding exercises
const AddExercise = ({ onAdd }) => {
  const [form, setForm] = useState({
    name: '',
    muscle_group: '',
    equipment: '',
  }); // form state

  const handleChange = (e) => {
    // update form fields when they change
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault(); // stop form from reloading the page
    await addExercise(form); // send the data to the backend
    onAdd(); // refresh the list
    setForm({ name: '', muscle_group: '', equipment: '' }); // clear the form
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Exercise</h2>
      <input
        type="text"
        name="name"
        placeholder="Name"
        value={form.name}
        onChange={handleChange}
      />
      <input
        type="text"
        name="muscle_group"
        placeholder="Muscle Group"
        value={form.muscle_group}
        onChange={handleChange}
      />
      <input
        type="text"
        name="equipment"
        placeholder="Equipment"
        value={form.equipment}
        onChange={handleChange}
      />
      <button type="submit">Add Exercise</button>
    </form>
  );
};

export default AddExercise;
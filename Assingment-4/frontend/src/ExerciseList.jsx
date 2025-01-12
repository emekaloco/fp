import React, { useEffect, useState } from 'react';
import { getExercises, deleteExercise, resetExercises } from './api';

// list of exercises, handles fetching and deleting them
const ExerciseList = () => {
  const [exercises, setExercises] = useState([]); // state for exercises

  // i fetch exercises when the component loads
  useEffect(() => {
    fetchExercises();
  }, []);

  const fetchExercises = async () => {
    // get exercises from the backend
    const data = await getExercises();
    setExercises(data); // update the state
  };

  const handleDelete = async (name) => {
    // deletes an exercise and refreshes the list
    await deleteExercise(name);
    fetchExercises();
  };

  const handleReset = async () => {
    // clears all exercises
    await resetExercises();
    fetchExercises();
  };

  return (
    <div>
      <h2>Exercise List</h2>
      <button onClick={handleReset}>Reset All</button>
      <ul>
        {exercises.map((exercise, index) => (
          <li key={index}>
            {exercise.name} - {exercise.muscle_group} - {exercise.equipment}
            <button onClick={() => handleDelete(exercise.name)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ExerciseList;
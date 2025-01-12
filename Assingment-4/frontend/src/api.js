import axios from 'axios';

// this is where the backend url is
const BASE_URL = 'http://127.0.0.1:5000';

// gets all the exercises from the backend
export const getExercises = async () => {
  const response = await axios.get(`${BASE_URL}/exercises`);
  return response.data;
};

// adds a new exercise
export const addExercise = async (exercise) => {
  const response = await axios.post(`${BASE_URL}/exercises`, exercise);
  return response.data;
};

// deletes an exercise by name
export const deleteExercise = async (name) => {
  const response = await axios.delete(`${BASE_URL}/exercises/${name}`);
  return response.data;
};

// resets all the exercises
export const resetExercises = async () => {
  const response = await axios.delete(`${BASE_URL}/exercises/reset`);
  return response.data;
};

// filters exercises by muscle group
export const filterExercises = async (muscleGroup) => {
  const response = await axios.get(`${BASE_URL}/exercises/filter`, {
    params: { muscle_group: muscleGroup },
  });
  return response.data;
};
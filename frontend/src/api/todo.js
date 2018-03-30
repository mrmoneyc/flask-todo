/* eslint no-console: ["error", { allow: ["dir", "warn", "error"] }] */
import axios from 'axios';

const getTodos = (cb) => {
  axios.get('http://localhost:5000/todo')
    .then((response) => {
      cb(response.data.result, null);
    })
    .catch((error) => {
      cb([], error.message);
    });
};

export default {
  getTodos,
};

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

const createTodo = (content, cb) => {
  const reqBody = { content };
  const reqHeader = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  axios.post('http://localhost:5000/todo', reqBody, reqHeader)
    .then((resp) => {
      console.dir(resp.data);
      cb(resp.data, null);
    })
    .catch((err) => {
      cb(null, err.message);
    });
};

export default {
  getTodos,
  createTodo,
};

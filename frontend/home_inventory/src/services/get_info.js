import fetch from "cross-fetch";

auth_code = "";

function get_info(auth_code) {
  const requestOptions = {
    method: "GET",
    accept: "application/json",
  };
  return fetch("http://127.0.0.1:8000/item?id=1", requestOptions)
    .then((response) => {
      response.json();
    })
    .then((res_json) => {
      console.log(res_json);
    });
}

import fetch from 'cross-fetch'

function login(username, password) {
    const data = { 'username': username, 'password': password }
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8' },
        body: `grant_type=password&username=${username}&password=${password}`
    }

    return fetch('http://127.0.0.1:8000/token', requestOptions)
        .then((response) => {
            return response.json();
        })
        .then((res_json) => {
            return res_json
        })

}

login('username', 'password')

export default login;
console.log('inside fetch example');


function getUsers(){
    console.log('clicked');
    fetch('https://reqres.in/api/users/').then(
        response => response.json()
    ).then(
        response_obj => put_users_inside_html(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function put_users_inside_html(response_obj_data) {
     console.log(response_obj_data);

    const curr_main = document.querySelector("main");
    let id = document.getElementById("id").value;
    for (let user of response_obj_data) {
        console.log(user.id)
        if (user.id == id){
            curr_main.innerHTML = `
            <img src="${user.avatar}" alt="Profile Picture"/>
            <div>
                <span>id: ${user.id}</span>
                <br>
                <span>Full name: ${user.first_name} ${user.last_name}</span>
                <br>
                 <span>Email: ${user.email}</span>
                <a href="mailto:${user.email}">Send Email</a> <br>
            </div>
            `;
        }

    }
}
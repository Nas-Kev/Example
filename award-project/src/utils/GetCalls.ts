const BASE_URL = "http://localhost:5000/";

export function getBestTeam() {
    return fetch(
        BASE_URL + "max_team",
        {
            method: "GET"
        }
    )
}

export function getBestLeader() {
    return fetch(
        BASE_URL + "max_leader",
        {
            method: "GET"
        }
    )
}


export function getBestMember() {
    return fetch(
        BASE_URL + "max_member",
        {
            method: "GET"
        }
    )
}

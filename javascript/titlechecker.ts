import { add_cookie } from "./cookie.js"
import { ready } from "jquery"
function substringsplit(str){
    const str_splitted = str.split(" ")
    return str_splitted
}

function charsplit(str){
    var char_splitted = [];
    for(let k = 0; k < str.length; k++){
        char_splitted.push(str[k]);
    }
    return char_splitted;
}

//FIXME: cookie not work 
class cookie{
    /**
     * 
     * @param {string | cookie} cookie_key_value_pair 
     */
    constructor(cookie_key_value_pair) {
        this.cookie_key_value_pair = cookie_key_value_pair;
    }

    add(){
        add_cookie(this.cookie_key_value_pair);

    }
    /**
     * 
     * @returns {string}
     * reads cookie value
     */
    read(){
        return getCookieValue(this.cookie_key_value_pair)
    }
    /**
     * @returns {cookie}
     */
    duplicate(){
        /**
         * @type {cookie}
         */
        const duplicate_ =cookie(this.cookie_key_value_pair);
        return duplicate_
    }
}

document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementsByTagName('title')[0].textContent == "A li'l trick i have in my sleeves") {
        document.getElementById("btn-1").addEventListener("click", function() {
            const doc_ =getCookieValue("Username");
            document.getElementById("af").innerText  = doc_
            console.log("this function got called id:1121")
        });
        
    }
    if (document.getElementsByTagName('title')[0].textContent ==
    "ICT - Programming")
    {
        document.getElementById("redirect-btn").addEventListener("click",function()
        {
            /**
             * @type {string}
             */
            const username =document.getElementById("mytrick").value
            Username=add_cookie("Username="+username)
            
            window.location.href = "./Beta.html"
        }
        );
    }
});


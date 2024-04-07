const cookies = document.cookie;
/**
 * 
 * @param {string} cookie_key_value_pair 
 */
function add_cookie(cookie_key_value_pair){
    document.cookie = cookie_key_value_pair+"; path=/";
    /**
     * add a cookie 
     * parameters: >>> cookie_key_value_pair must be separated
     */
}

const logger = console.log;

/**
 * Retrieve the value of the specified cookie key.
 * 
 * @param {string} cookieKey - The key of the cookie to retrieve.
 * @returns {string|null} The value of the cookie, or null if the cookie is not found.
 */
function getCookieValue(cookieKey) {
    // Split the document.cookie string into an array of individual cookies
    var cookiesArray = document.cookie.split(';');
  
    // Loop through each cookie to find the one with the specified key
    for (var i = 0; i < cookiesArray.length; i++) {
        var cookie = cookiesArray[i];

        cookie = cookie.trim();
        // Check if this cookie starts with the desired key
        if (cookie.indexOf(cookieKey + '=') === 0) {
            // Extract and return the value of the cookie
            return cookie.substring(cookieKey.length + 1);
        }
    }
    // Return null if the cookie is not found
    return null;
}

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
            add_cookie("Username="+username)
            window.location.href = "./Beta.html"
        }
        );
    }
});

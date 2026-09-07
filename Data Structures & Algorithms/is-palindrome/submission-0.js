class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */

   

    isPalindrome(s) {


        let removeNonAlphanumeric = s.replace(/[^a-zA-Z0-9]/g, "").toLocaleLowerCase()
        let inputStr =  removeNonAlphanumeric.trim();
        let reversedStr = inputStr.split("").reverse().join("");
        console.log(inputStr, reversedStr);
        if(inputStr === reversedStr){
            return true;
        } else {
            return false;
        }

    }
}

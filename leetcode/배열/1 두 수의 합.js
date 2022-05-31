const nums = [2,7,11,15];
const target = 9;
let output = [];

for (let i = 0; i < nums.length; i++){
    let sum = 0;
    for (let j = i; j < nums.length; j++){
        sum = nums[i] + nums[j];
        if (sum == target){
            output = [i, j];
        }
    }
}

console.log(output);
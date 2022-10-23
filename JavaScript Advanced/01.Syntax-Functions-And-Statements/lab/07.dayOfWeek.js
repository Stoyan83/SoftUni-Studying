function solve(input){
    const days = {
        'Sunday': 7,
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6
      }
      if(input in days){
        console.log(days[input]);
      }else{
        console.log(`error`);
      }
    }

solve('Friday')
solve('Invalid')
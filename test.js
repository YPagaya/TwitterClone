var sortNumber = function (number) {
    number.sort(function (a, b) {
        if (a == b) {
            return 0;
        }
        return a < b ? -1 : 1;
    });
 };
 
 var number = [19, 3, 81, 24, 21,5];
 sortNumber(number);
 console.log(number);

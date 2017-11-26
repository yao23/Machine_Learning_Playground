select distinct Num as ConsecutiveNums
from
(
    select Num, 
           (
            case when @prev <> (@prev := Num) then @consecutive_cnt := 1
                 else @consecutive_cnt :=  @consecutive_cnt + 1
            end
           ) as consecutive_cnt
    from Logs,
         (
          select @consecutive_cnt := 0, 
                 @prev := (select Num from Logs limit 1)
         ) as init
) as t
where consecutive_cnt = 3;




select distinct t1.Num as ConsecutiveNums
from Logs t1, Logs t2, Logs t3
where t1.Id = t2.Id - 1 and t2.Id = t3.Id -1
      and t1.Num = t2.Num and t2.Num = t3.Num
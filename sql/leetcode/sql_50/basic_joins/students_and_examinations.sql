select
    st.student_id,
    st.student_name,
    su.subject_name,
    count(e.subject_name) as attended_exams
from students as st
cross join subjects as su
left outer join
    examinations as e
    on st.student_id = e.student_id and su.subject_name = e.subject_name
group by st.student_id, st.student_name, su.subject_name
order by st.student_id asc, su.subject_name asc;

Select b.unique_id, a.name From Employees a
LEFT JOIN EmployeeUNI b on b.id=a.id;

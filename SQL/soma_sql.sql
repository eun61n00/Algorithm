select concat(regexp_replace(id, '[0-9]', ''), lpad(regexp_replace(right(id, 4), '[a-z]', ''), 4, '0')), id as original_id
from users;


select regexp_replace(id, '[0-9]', ''), lpad(regexp_replace(right(id, 4), '[a-z]', ''), 4, '0')
from users;


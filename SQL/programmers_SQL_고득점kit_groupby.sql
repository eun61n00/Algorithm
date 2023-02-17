-- programmers SQL 고득점 kit
-- GROUP BY


-- 진료과별 총 예약 횟수 출력하기
SELECT MCDP_CD AS '진료과코드', COUNT(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE APNT_YMD LIKE '2022-05-%'
GROUP BY MCDP_CD
ORDER BY 5월예약건수, 진료과코드
-- ORDER BY '5월예약건수', '진료과코드' (오답: https://dev.mysql.com/doc/refman/8.0/en/problems-with-alias.html)


-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(*) AS 'count'
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

-- 입양 시각 구하기(1)
SELECT HOUR(DATETIME) AS 'HOUR', COUNT(ANIMAL_ID) AS 'COUNT'
FROM ANIMAL_OUTS
GROUP BY HOUR
HAVING HOUR BETWEEN 9 AND 19
ORDER BY HOUR


-- 입양 시각 구하기(2)
-- 변수 설정
SET @hour := -1;
SELECT (@hour := @hour + 1) AS 'HOUR'
FROM ANIMAL_OUTS
WHERE @hour < 23;

SET @hour := -1;
SELECT (@hour := @hour + 1) AS 'HOUR',
    (SELECT COUNT(*) FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @hour) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;


-- 가격대 별 상품 개수 구하기
SELECT (PRICE div 10000) * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCTS
FROM PRODUCT
GROUP BY (PRICE div 10000)
ORDER BY PRICE_GROUP
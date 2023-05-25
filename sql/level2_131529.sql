-- 코드를 입력하세요
SELECT
  LEFT(PRODUCT_CODE, 2) AS CATEGORY,
  COUNT(*) AS PRODUCTS
FROM
  PRODUCT
GROUP BY
  CATEGORY
ORDER BY
  CATEGORY

-- LEFT(문자, 숫자) : 문자의 처음부터 숫자개만큼 추출
-- RIGHT(문자, 숫자) : 문자의 마지막부터 숫자개만큼 추출
-- MID(문자, 시작할 위치, 숫자) : 문자의 시작할 위치부터 숫자개만큼 추출

-- 예시
-- LEFT('ABCDE', 2) : 'AB'
-- RIGHT('ABCDE', 2) : 'DE'
-- MID('ABCDE', 2, 2) : 'BC'
-- SUBSTR('ABCDEFG', 2, 4) : 'BCDE'
-- SUBSTRING('ABCDEFG', 2, 4) : 'BCDE'
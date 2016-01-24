mongo localhost/new_adn create_user.js 
echo '====== ERROR ==========================='
mongo localhost/new_adn -uadmin -padmi
echo '====== RIGHT ==========================='
mongo localhost/new_adn -uadmin -padmin

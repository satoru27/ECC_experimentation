import gmpy2, time
from gmpy2 import mpz,mpq,mpfr,mpc
#testing a large number
#out = mpz(218739823698213692186392817398217392183219836219362913692136299129328732813792872193213982713981273971298721931328321362193621936291392163289163918392183629163921863921632187213) * mpz(828398213629816392139286329369216392836298362198362193621321128379821739217398217391273921783221837128937219837219837918738927389217398217398729372198379812738912739872183972981379812739127398217398127389217398217312313)
#print(out)
#print(gmpy2.is_prime(out))

#print("--- \tstart\t ---")
#start = time.time()
#prime = pow(mpz(2),20996011) -1
#print(prime)
#print("--- \t%s seconds\t ---" % (time.time() - start))

start = time.time()
print("--- \tstart\t ---")
prime2 = mpz(1)
for i in range (1,6918):
	prime2 *= mpz(i)

prime2 -= 1
print(prime2)
print("--- \t%s seconds\t ---" % (time.time() - start))


print("--- \tstart\t ---")
start = time.time()
print(gmpy2.is_prime(2011))
print("--- \t%s seconds\t ---" % (time.time() - start))
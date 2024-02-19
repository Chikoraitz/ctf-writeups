# Description

> AUTHOR: SARA
>
> #### Description
>
> In RSA, a small `e` value can be problematic, but what about `N`? Can you decrypt this? [values](https://mercury.picoctf.net/static/b9ddda080c56fb421bf30409bec3460d/values)

---

> Decrypt my super sick RSA:
> c: 964354128913912393938480857590969826308054462950561875638492039363373779803642185
> n: 1584586296183412107468474423529992275940096154074798537916936609523894209759157543
> e: 65537



# *RSA*

From [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem)): 

> *RSA* is one of the oldest public-key cryptosystem. In public-key cryptosystems, the encryption key is public and distinct from the decryption (private) key. An *RSA* user creates and publishes a public key based on two secret large prime numbers, along with an auxiliary value. The security of *RSA* relies on the practical difficulty of factoring the product of two large prime numbers - [factoring problem](https://en.wikipedia.org/wiki/Factoring_problem). Breaking *RSA* encryption is known as the [RSA problem](https://en.wikipedia.org/wiki/RSA_problem). There are no published methods to defeat the system if a large enough key is used.
>
> *RSA* is a relatively slow algorithm. Because of this, it is not commonly used to directly encrypt user data. More often, *RSA* is used to transmit shared keys for symmetric-key cryptography, which are then used for bulk encryption–decryption.



The algorithm is a 4-step process:

- **Key generation**

  - Select two (large) prime numbers $p$ and $q$.

  - $p$ and $q$ should be chosen at random, large, have a large difference, and be kept **secret**.

  - $n = p q$ : $n$ is <u>used as the modulus for both the public and private keys</u>. Its length, usually expressed in bits, is the key length.

  - Compute the *Carmichael's totient function* $\lambda(n)$. 

    In the context of computing the *RSA* pair of keys, the *Euler's totient function* $\phi(n)$ can also be used, in fact, it is the function used in the original *RSA* paper.

    - Since $n = pq$, $\phi(n) = lcm(\lambda(p), \lambda(q))$. 
    - Since $p$ and $q$ are prime, $λ(p) = \phi(p) = p − 1$, and likewise $\lambda(q) = q − 1$. Hence $\lambda(n) = lcm(p − 1, q − 1) = (p − 1)(q − 1)$.
    - $\lambda(n)$ should be kept **secret**.

  - Choose an integer $e$ such that $1 < e < \lambda(n)$, and needs to be coprime with $n$ and $\lambda(n)$.  $e$ is released as <u>part of the public key</u>.

  - Compute $d$, such that $d e (mod\quad \lambda(n)) = 1$. In other words, $d$ is the multiplicative inverse of $e$ in $(mod\quad\phi(n))$.

    $d$ is the private key exponent and should be kept **secret**.

- **Key distribution**

  Suppose that *Bob* wants to send information to *Alice*. If they decide to use *RSA*, *Bob* must know *Alice's* public key to encrypt the message, and *Alice* must use her private key to decrypt the message. To enable *Bob* to send his encrypted messages, *Alice* transmits her public key $(e, n)$ to *Bob* via a reliable, but not necessarily secret, route. *Alice's* private key ($d$) is never distributed.

- **Key encryption**

  To send a message to *Alice*, *Bob* turns the message into an integer $m$ and computes the ciphertext $c$, using *Alice's* public key $e$ : $c = m^e (mod\quad n)$. 

- **Key decryption**

  *Alice* can recover the original message $m$ from $c$ using the private key exponent $d$: $m = c^d (mod\quad n)$



# Solution

If $p$ and $q$ were somehow found, $\phi(n)$ can be computed and since $e$ is released as part of the public key, $d$ can also be computed. Hence, finding $d$ is a prime factorization problem. To find the factors, we can use the [`FactorDB`](https://factordb.com/) database to find known factorizations for any number.

The `p` and `q` of the provided `n` are respectively: `2434792384523484381583634042478415057961` and `650809615742055581459820253356987396346063`. 

```python
from Crypto.Util.number import inverse, long_to_bytes
phi_n = (p-1)*(q-1)
d = inverse(e,phi_n)
m = pow(c,d,n)
printf(long_to_bytes(m))
```


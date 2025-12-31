# Insecure Deserialization Explained

### The Concept
Serialization is turning an object (like a User Profile) into a stream of bytes to save it to a file or network. Deserialization is the reverse.
**Insecure** Deserialization happens when the application blindly trusts the stream of bytes and reconstructs the object without validation.

**The Analogy:**
Imagine you are moving houses. You pack (serialize) your furniture into boxes.
* **Secure:** You unpack the boxes and put the furniture in the new house.
* **Insecure:** You receive a box from a stranger labeled "Lamp". When you open it (deserialize), a spring-loaded snake jumps out and bites you. The process of *opening* the box triggered the attack.

### The Flaw
Python's `pickle` module is not secure against erroneous or maliciously constructed data. It allows objects to define a `__reduce__` method, which can specify a function to run during unpickling.
If an attacker sends a pickled object that says "Run `os.system('rm -rf /')` when you open me," the server will obey.

### The Fix
Do not use `pickle`, `Ruby Marshal`, or `Java ObjectSerialization` for untrusted data.
Use **JSON**. JSON is a data-interchange format, not an object-serialization format. It can hold strings and numbers, but it cannot hold executable code or class definitions.
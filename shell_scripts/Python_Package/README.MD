# Automating the process of building,testing and deploying a Python Package

# Requirements:

```python
pip install twine
```

Usage:

1. Make it executable

```
chmod +x lets_build.sh
```

2. Go to https://test.pypi.org/ and create your account

3. Test your package:

```
 ./lets_build.sh --test
```

4. Now publish your publis

```
 ./lets_build.sh 
```
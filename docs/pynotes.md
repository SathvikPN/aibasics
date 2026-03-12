refer: https://algomaster.io/learn/python/classes-objects

```
CtrlD - EOF

functions: {
    params are passed by object reference (loosley pass by reference - reference changes if object is immutable)
    - local function var point to same reference of outside object,
    - if of type immutable, updating var makes local var points to new object refernce 
    - if mutable (list, dict, set) updates external var value.

    def range(start, stop=None, step=1) -- default params
}
```


<details> 
<summary> function signatures </summary>


### FUNCTIONS ================================================================================================

# Function Definition showcasing different parameter types
def configure_system(
    task_name: str,                         # 1. Standard Positional Argument (Required)
    priority: int = 1,                      # 2. Argument with Default Value (Optional)
    *,                                      # 3. Separator for Keyword-Only Arguments
    log_file: str = "system.log",           # 4. Keyword-Only Argument (Must be called by name)
    flags: List[str]                        # 5. Required Keyword-Only Argument
) -> str:
    return f"Task '{task_name}' configured successfully."

# --- DEMONSTRATION CALLS ---

# A. Standard Call (Positional Args)
configure_system("INIT", flags=["v", "d"]) # priority defaults to 1

# B. Call using Keyword Arguments for flexibility
configure_system(task_name="NETWORK_TEST", priority=5, flags=["net-verbose"])

# C. Call demonstrating the Keyword-Only Restriction
# Note: You CANNOT pass 'log_file' or 'flags' positionally after the '*'
configure_system("DATABASE_MIGRATE", 10, log_file="db.log", flags=["sql"]) 
```

</details>
```mermaid
classDiagram
    Dataset *-- SpecInf
    
    class Dataset {
        +string name_exp
        +datetime date
        +string compound
        +string sample_id
        +SpecInf spec_inf
    }
    
    class SpecInf {
        +float[0..*] wl
        +float wl_ratio
        +string anode
        +float steptime
        +float stepsize
        +float start
        +float theta
        +float theta2
    }
    
```
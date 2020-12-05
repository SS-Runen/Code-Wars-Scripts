

#INCOMPLETE
"""
Unable to avoid Julia behaviour of automatically converting array
elements' type. Boolean `false` is automatically being converted
to zero on array instantiation with false and other numeric
elements. If instantiated with any one string element, array
does not convert false to integer or float.

When attemp was made to push! the string "string" into the Float array,
Julia threw an error stating that the string could not be
implicitly converted into a Float.
"""


function move_zeroes(array::Array)
    new_array = Array([])
    zeroes_array = Array([])

    for item in array
        if (typeof(item) != Bool) && item == 0
            push!(zeroes_array, item)
        else
            push!(new_array, item)
            println(item)
        end
    end

    append!(new_array, zeroes_array)
    println(length(zeroes_array))
    return new_array
end

first_test = [
    false, 9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3,
    0, 1, 9, 0, 0, 0, 0, 9
        ]

result = move_zeroes(first_test)

println(first_test)
println(result)

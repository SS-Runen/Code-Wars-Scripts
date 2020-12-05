"""
Input: String containing different "words" separated by spaces.

1. More than one word? Reverse each word and combine first with second,
third with fourth and so on.
An odd number of words means last one stays alone but has to be reversed too.

2. Start it again until there's only one word without spaces.

3. Return your result.

Ex:
"abc def" => "cbafed"
"""


function reverse_strings(string::String)
    string_array = split(string)
    iterations_needed = ceil(length(string_array)/2)
    println("Iterations needed:", iterations_needed)    
    iterations_done = 0
    println("Iterations done:", iterations_done)

    #while (length(string_array) != 1)
    while (iterations_done != iterations_needed)
        new_array = []
        array_length = length(string_array)

        for index in 1:array_length
            string_array[index] = reverse(string_array[index])            
        end

        for index in range(1, array_length, step = 2)
            if !((index + 1) > length(string_array))
                joined_words = join([string_array[index], string_array[index + 1]])
                push!(new_array, joined_words)
            else
                push!(new_array, string_array[index])
            end
        end

        #println("String array: ", string_array)
        string_array = new_array
        iterations_done += 1

    end

    return join(string_array)

end


function join_pairs!(string_array::Array)
    new_array = []

    for index in range(1, length(string_array), step = 2)

        if !((index + 1) > length(string_array))
            joined_pair = join([string_array[index], string_array[index + 1]])
            push!(new_array, joined_pair)
        else
            push!(new_array, string_array[index])
        end

    end

    return new_array

end


function reverse_strings_b(string::String)
    string_array = split(string)        

    while (length(string_array) != 1)            
        array_length = length(string_array)

        for index in 1:array_length
            string_array[index] = reverse(string_array[index])            
        end

        #for word in string_array
         #   word = reverse(word)
        #end

        string_array = join_pairs!(string_array)
        #println("String array: ", string_array)        

    end

    return join(string_array)

end

input_2 = "abc def"
input_3 = "abc def hij"
input_6 = "abc def hij abc def hij"

println("Input `$input_2`: ", reverse_strings(input_2))
println("Input `$input_3`: ", reverse_strings(input_3))
println("Input `$input_6`: ", reverse_strings(input_6))

println("Called function with separate joining function with `$input_2`:\n", reverse_strings_b(input_2))
println("Called function with separate joining function with `$input_3`:\n", reverse_strings_b(input_3))
println("Called function with separate joining function with `$input_6`:\n", reverse_strings_b(input_6))

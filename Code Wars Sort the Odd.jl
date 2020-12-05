

function sort_array(array)
    odd_numbers = []
    odd_number_indexes = []
    new_array = copy(array)

    for index in 1:length(array)
        number = array[index]
        if isodd(number)
            push!(odd_numbers, number)
            push!(odd_number_indexes, index)
        end
    end       
    
    while true
        ctr_unordered_pairs = 0

        for index in 1:(length(odd_numbers) - 1)
            first = odd_numbers[index]
            second = odd_numbers[index + 1]

            if first > second
                odd_numbers[index] = second
                odd_numbers[index + 1] = first
                ctr_unordered_pairs += 1
            end

        end

        if ctr_unordered_pairs == 0
            break
        end
    
    end

    counter = 1
        
    for index in odd_number_indexes
        new_array[index] = odd_numbers[counter]
        counter += 1
    end

    println("Odd indexes: ", odd_number_indexes)
    return new_array

end

"""
function sort_array_b(array)
    odd_numbers = Dict()
    new_array = copy(array)

    for index in 1:length(array)
        number = array[index]

        if isodd(number)
            push!(odd_numbers, index => number)            
        end
    end

    odd_number_indexes = keys(odd_numbers)

    ctr_unordered_pairs = 1

    while ctr_unordered_pairs >= 1
        ctr_unordered_pairs = 0

        for index in 1:(length(odd_number_indexes) - 1)
            first = odd_numbers[odd_number_indexes[index]]
            second = odd_numbers[odd_number_indexes[index + 1]]

            if first > second
                odd_numbers[odd_number_indexes[index]] = second
                odd_numbers[odd_number_indexes[index + 1]] = first
                ctr_unordered_pairs += 1
            end
        end

    end

    for odd_number_index in keys(odd_numbers)
        new_array[odd_number_index] = odd_numbers[odd_number_index]
    end

    println("Odd indexes: ", odd_number_indexes)
    return new_array
end
"""

function sort_array_c(array)
    odd_numbers = []
    odd_number_indexes = []
    new_array = copy(array)

    for index in 1:length(array)
        number = array[index]
        if isodd(number)
            push!(odd_numbers, number)
            push!(odd_number_indexes, index)
        end
    end       
    
    sort!(odd_numbers)

    counter = 1
        
    for index in odd_number_indexes
        new_array[index] = odd_numbers[counter]
        counter += 1
    end

    println("Odd indexes: ", odd_number_indexes)
    return new_array

end


input = [5, 3, 2, 8, 1, 4]
println("Input ", input)
println("Called sort_array: ", sort_array(input))
#println("Called sort_array_b: ", sort_array_b(input))
println("Called sort_array_c: ", sort_array_c(input))

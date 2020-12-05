"""
Decrypt method for Julia has apparently wrong steps but still works.
Conversely, the copy of the Python script section gives wrong innput.
- Tried switching to while-loop, same results.
- Tried switching the order of pushing char from firsts and seconds.
Gave wrong answer.
- Set iterations_done = 1 intead of zero then using python algorithm.
Python steps only worked on second test using 5 iterations and odd input.
Steps that shouldn't work still gave correct input.

Julia script appends! or pushes! all the seconds then all the firsts.
Proper procedure is to push in a first, push in a second recursively.
Encryption:
1. Group letters into pairs. From the pairs, distinguish firsts and seconds.
2. Put all second letters in output string.
3. Append all first letters to the output string.
4. Repeat for specified iterations.
"""

function encrypt(str::String, n::Int)
    text_length = length(str)
    arr_encrypted_text = [char for char in str]

    for ctr in 1:n        
        firsts, seconds = [], []

        for index in 1:text_length
            
            if (index & 1) == 1
                push!(firsts, arr_encrypted_text[index])
            else
                push!(seconds, arr_encrypted_text[index])
            end

        end
        
        empty!(arr_encrypted_text)        
        #append!(arr_encrypted_text, seconds, firsts)
        append!(arr_encrypted_text, seconds)
        append!(arr_encrypted_text, firsts)
        
        #for char in seconds
         #   push!(arr_encrypted_text, char)
        #end

        #for char in firsts
         #   push!(arr_encrypted_text, char)
        #end

    end

    return join(arr_encrypted_text)

end


function decrypt(str::String, n::Int)
    arr_text = [char for char in str]
    text_length = length(str)
    floordiv_half = Int(floor(text_length/2))
    #iterations_done = 1

    #while iterations_done < n                
    for ctr in 1:n
        firsts = arr_text[(floordiv_half + 1):text_length]
        seconds = arr_text[1:floordiv_half]

        empty!(arr_text)
        append!(arr_text, seconds)
        append!(arr_text, firsts)
        
        #Method that should not work: add seconds then add firsts.
        """
        for char in seconds
            push!(arr_text, char)
        end

        for char in firsts
            push!(arr_text, char)
        end
        """   

        #Copy of method in Python script. Doesn't work though it should.
        """
        for index in 1:floordiv_half
            push!(arr_text, seconds[index])
            push!(arr_text, firsts[index])
        end

        if (floordiv_half * 2) < text_length
            push!(arr_text, firsts[floordiv_half + 1])
        end
        """
        #iterations_done += 1

    end

    return join(arr_text)

end


function test_input(lst_strs::Array{String}, iter::Int)
    
    for string in lst_strs
        #println("\n=====\nOriginal:\n\t$str")
        encrypted_text = encrypt(string, iter)
        decrypted_text = decrypt(string, iter)
        
        println("\n=====\nOriginal:\n\t$string")
        println("Encrypted:\n\t", encrypted_text)
        println("Decrypted:\n\t", decrypted_text)
    end
    
end


even_input = "This is even! End."
odd_input = "This is odd. End."

test_input([even_input, odd_input], 5)
test_input([even_input, odd_input], 8)

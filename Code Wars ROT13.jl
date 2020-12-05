

function ROT13(str::String)
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_shifted = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZabcdefghijklm"
    array_encrypted_text = []
    shift_table = Dict([])

    for index in 1:length(alphabet)
        push!(shift_table, alphabet[index] => alphabet_shifted[index])
    end

    for char in str
        if char in alphabet
            push!(array_encrypted_text, shift_table[char])
        else
            push!(array_encrypted_text, char)
        end
        
    end

    return join(array_encrypted_text)

end

str_input = "EBG13 rknzcyr. mnmn"
println(ROT13(str_input))

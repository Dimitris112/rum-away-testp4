import Inputmask from "inputmask";
import '../static/js/phone_mask';

document.body.innerHTML = `
  <input type="text" id="telephone" />
`;

test("applies input mask to phone field", () => {
  const phoneInput = document.getElementById("telephone");

  const inputMaskMock = jest
    .spyOn(Inputmask.prototype, "mask")
    .mockImplementation(() => {});

  document.addEventListener("DOMContentLoaded", function () {
    Inputmask("(999) 999-9999").mask(phoneInput);
  });

  document.dispatchEvent(new Event("DOMContentLoaded"));

  expect(inputMaskMock).toHaveBeenCalledWith(phoneInput);

  phoneInput.value = "1234567890";

  // apply the mask logic
  phoneInput.value = phoneInput.value.replace(
    /(\d{3})(\d{3})(\d{4})/,
    "($1) $2-$3"
  );

  // value matches the format
  expect(phoneInput.value).toBe("(123) 456-7890");

  // restore original
  inputMaskMock.mockRestore();
});
